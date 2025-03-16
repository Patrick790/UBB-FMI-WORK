package com.network.rpcprotocol;

import com.example.Participant;
import com.example.Race;
import com.example.Registration;
import com.example.User;
import com.services.IMotorcyclesObserver;
import com.services.IMotorcyclesServices;
import com.services.MotorcyclesException;
import com.services.Observer;

import java.io.EOFException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.Socket;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;
import java.util.Optional;

public class MotorcyclesClientRpcReflectionWorker implements Runnable, Observer{

    private IMotorcyclesServices server;
    private Socket connection;

    private ObjectInputStream input;

    private ObjectOutputStream output;
    private volatile boolean connected;

    public MotorcyclesClientRpcReflectionWorker(IMotorcyclesServices server, Socket connection) {
        this.server = server;
        this.connection = connection;
        try {
            output = new ObjectOutputStream(connection.getOutputStream());
            output.flush();
            input = new ObjectInputStream(connection.getInputStream());
            connected = true;
            server.registerObserver(this);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    @Override
    public void run() {
        while (connected) {
            try {
                if (!connection.isClosed()) {
                    Object request = input.readObject();
                    Response response = handleRequest((Request) request);
                    if (response != null) {
                        sendResponse(response);
                    }
                }
            } catch (EOFException e) {
                System.out.println("End of stream reached unexpectedly: " + e);
            } catch (IOException e) {
                e.printStackTrace();
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            }
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        try {
            input.close();
            output.close();
            connection.close();
        } catch (IOException e) {
            System.out.println("Error " + e);
        }
    }

    private static Response okResponse = new Response.Builder().type(ResponseType.OK).build();

    private Response handleRequest(Request request){
        Response response=null;
        String handlerName="handle"+(request).type();
        System.out.println("HandlerName "+handlerName);
        try {
            Method method=this.getClass().getDeclaredMethod(handlerName, Request.class);
            response=(Response)method.invoke(this,request);
            System.out.println("Method "+handlerName+ " invoked");
        } catch (NoSuchMethodException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        }

        return response;
    }

    private Response handleADD_REGISTRATION(Request request) throws MotorcyclesException, SQLException {
        System.out.println("Add registration request ..." + request.type());
        Registration registration = (Registration) request.data();
        server.addRegistration(registration);
        return okResponse;
    }

    private Response handleLOGIN(Request request){
        System.out.println("Login request ..."+request.type());

        Map<String, String> loginData = (Map<String, String>)request.data();
        String username = loginData.get("username");
        String password = loginData.get("password");
        try {
            boolean loggedIn = server.login(username, password, this);
            if (loggedIn) {
                return okResponse;
            } else {
                connected = false;
                return new Response.Builder().type(ResponseType.ERROR).data("Login failed").build();
            }
        } catch (MotorcyclesException e) {
            connected = false;
            return new Response.Builder().type(ResponseType.ERROR).data(e.getMessage()).build();
        }
    }



    private Response handleGET_ALL_RACES(Request request){
        System.out.println("Get all races request ..."+request.type());
        try {
            Iterable<Race> races = server.getAllRaces();
            return new Response.Builder().type(ResponseType.OK).data(races).build();
        } catch (MotorcyclesException e) {
            return new Response.Builder().type(ResponseType.ERROR).data(e.getMessage()).build();
        }
    }

    private Response handleGET_NEXT_PARTICIPANT_ID(Request request) throws MotorcyclesException {
        System.out.println("Get next participant ID request ..." + request.type());
        long nextId = server.getNextParticipantId();
        return new Response.Builder().type(ResponseType.GET_NEXT_PARTICIPANT_ID).data(nextId).build();
    }

    private Response handleADD_RACE(Request request) throws SQLException, MotorcyclesException {
        System.out.println("Add race request ..." + request.type());
        Race race = (Race) request.data();
        server.addRace(race);
        server.notifyAllObservers();
        return okResponse;
    }

    private Response handleFIND_PARTICIPANT_BY_NAME_TEAM(Request request) throws MotorcyclesException {
        System.out.println("Find participant by name and team request ..." + request.type());
        Map<String, String> participantData = (Map<String, String>) request.data();
        String name = participantData.get("name");
        String team = participantData.get("team");
        Optional<Participant> participantOpt = server.findParticipantByNameAndTeam(name, team);
        Participant participant = participantOpt.orElse(null); // Convert Optional to nullable object
        return new Response.Builder().type(ResponseType.FIND_PARTICIPANT_BY_NAME_TEAM).data(participant).build();
    }

    private Response handleIS_PARTICIPANT_REGISTERED_FOR_RACE(Request request) throws MotorcyclesException {
        System.out.println("Is participant registered for race request ..." + request.type());
        // Assuming the request data is a Map object
        Map<String, Object> registrationData = (Map<String, Object>) request.data();
        Participant participant = (Participant) registrationData.get("participant");
        Race race = (Race) registrationData.get("race");
        boolean isRegistered = server.isParticipantRegisteredForRace(participant, race);
        return new Response.Builder().type(ResponseType.IS_PARTICIPANT_REGISTERED_FOR_RACE).data(isRegistered).build();
    }



    private Response handleADD_USER(Request request) throws MotorcyclesException {
        System.out.println("Add user request ..." + request.type());
        User user = (User) request.data();
        server.addUser(user);
        return okResponse;
    }

    private Response handleADD_PARTICIPANT(Request request) throws MotorcyclesException, SQLException {
        System.out.println("Add participant request ..." + request.type());
        Participant participant = (Participant) request.data();
        server.addParticipant(participant);
        server.notifyAllObservers();
        return okResponse;
    }

    private Response handleFIND_AFTER_USERNAME(Request request) throws MotorcyclesException {
        System.out.println("Find after username request ..." + request.type());
        String username = (String) request.data();
        User user = server.findAfterUsername(username);
        return new Response.Builder().type(ResponseType.FIND_AFTER_USERNAME).data(user).build();
    }


    private Response handleSEARCH_BY_TEAM(Request request) throws MotorcyclesException {
        System.out.println("Search participant request ..." + request.type());
        // Assuming the request data is a String representing the name of the participant
        String team = (String) request.data();
        List<Participant> participants = server.findByTeam(team);
        return new Response.Builder().type(ResponseType.SEARCHED_BY_TEAM).data(participants).build();
    }


    private Response handleHASH_PASSWORD(Request request) throws MotorcyclesException {
        System.out.println("Hash password request ..." + request.type());
        String password = (String) request.data();
        String hashedPassword = server.hashPassword(password);
        return new Response.Builder().type(ResponseType.HASH_PASSWORD).data(hashedPassword).build();
    }




private Response handleCOUNT_REGISTRATIONS_FOR_RACE(Request request) throws MotorcyclesException, SQLException {
    System.out.println("Count registrations for race request ..." + request.type());
    Race race = (Race) request.data();
    int count = server.countRegistrationsForRace(race);
    return new Response.Builder().type(ResponseType.COUNT_REGISTRATIONS_FOR_RACE).data(count).build();
}


    private Response handleGET_CAPACITY_FOR_PARTICIPANT(Request request) throws MotorcyclesException {
        System.out.println("Get capacity for participant request ..." + request.type());
        Participant participant = (Participant) request.data();
        int capacity = server.getCapacityForParticipant(participant);
        return new Response.Builder().type(ResponseType.GET_CAPACITY_FOR_PARTICIPANT).data(capacity).build();
    }




    private void sendResponse(Response response) throws IOException{
        System.out.println("sending response "+response);
        synchronized (output) {
            output.writeObject(response);
            output.flush();
        }
    }


    @Override
    public void update() throws SQLException, MotorcyclesException {
        System.out.println("A new race has been added.");


    }
}
