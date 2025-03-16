package com.network.rpcprotocol;


import com.example.Participant;
import com.example.Race;
import com.example.Registration;
import com.hibernate.user.User;
import com.services.IMotorcyclesObserver;
import com.services.IMotorcyclesServices;
import com.services.MotorcyclesException;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public class MotorcyclesServicesRpcProxy implements IMotorcyclesServices {

    private final String host;

    private final int port;

    private IMotorcyclesObserver client;

    private ObjectInputStream input;

    private ObjectOutputStream output;

    private Socket connection;

    private BlockingQueue<Response> qresponses;

    private volatile boolean finished;

    public MotorcyclesServicesRpcProxy(String host, int port) {
        this.host = host;
        this.port = port;

        qresponses = new LinkedBlockingQueue<Response>();
    }


    @Override
    public Iterable<Participant> getAllParticipants() throws MotorcyclesException {
        initializeConnection();
        Request request = new Request.Builder().type(RequestType.GET_ALL_PARTICIPANTS).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            closeConnection();
            throw new MotorcyclesException((String) response.data());
        }
        return (Iterable<Participant>) response.data();
    }

    @Override
    public void addParticipant(Participant participant) throws MotorcyclesException {
        initializeConnection();
        Request request = new Request.Builder().type(RequestType.ADD_PARTICIPANT).data(participant).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            closeConnection();
            throw new MotorcyclesException((String) response.data());
        }
    }


    @Override
    public List<Participant> findByTeam(String team) throws MotorcyclesException {
        initializeConnection();
        Request request = new Request.Builder().type(RequestType.SEARCH_BY_TEAM).data(team).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            closeConnection();
            throw new MotorcyclesException((String) response.data());
        }
        return (List<Participant>) response.data();
    }

    @Override
    public Optional<Participant> findParticipantByNameAndTeam(String name, String team) throws MotorcyclesException {
        initializeConnection();
        Map<String, String> participantData = new HashMap<>();
        participantData.put("name", name);
        participantData.put("team", team);
        Request request = new Request.Builder().type(RequestType.FIND_PARTICIPANT_BY_NAME_TEAM).data(participantData).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            closeConnection();
            throw new MotorcyclesException((String) response.data());
        }
        Participant participant = (Participant) response.data();
        return participant != null ? Optional.of(participant) : Optional.empty();
    }

    @Override
    public Iterable<Race> getAllRaces() throws MotorcyclesException {
        initializeConnection();
        Request request = new Request.Builder().type(RequestType.GET_ALL_RACES).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            closeConnection();
            throw new MotorcyclesException((String) response.data());
        }
        return (Iterable<Race>) response.data();
    }

    @Override
    public void addRace(Race race) throws MotorcyclesException {
        initializeConnection();
        Request request = new Request.Builder().type(RequestType.ADD_RACE).data(race).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            closeConnection();
            throw new MotorcyclesException((String) response.data());
        }
    }

    @Override
    public void addRegistration(Registration registration) throws MotorcyclesException {
        initializeConnection();
        Request request = new Request.Builder().type(RequestType.ADD_REGISTRATION).data(registration).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            closeConnection();
            throw new MotorcyclesException((String) response.data());
        }
    }

    @Override
    public int countRegistrationsForRace(Race race) throws MotorcyclesException {
        initializeConnection();
        Request request = new Request.Builder().type(RequestType.COUNT_REGISTRATIONS_FOR_RACE).data(race).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            closeConnection();
            throw new MotorcyclesException((String) response.data());
        }
        return (int) response.data();
    }

    @Override
    public int getCapacityForParticipant(Participant participant) throws MotorcyclesException {
        initializeConnection();
        Request request = new Request.Builder().type(RequestType.GET_CAPACITY_FOR_PARTICIPANT).data(participant).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            closeConnection();
            throw new MotorcyclesException((String) response.data());
        }
        return (int) response.data();
    }

    @Override
    public boolean login2(String username, String password) {
        return false;
    }

    @Override
    public boolean login(String username, String password, IMotorcyclesObserver client) throws MotorcyclesException {
        initializeConnection();
        Map<String, String> loginData = new HashMap<>();
        loginData.put("username", username);
        loginData.put("password", password);
        System.out.println("client in rpc proxy: " + client);
        Request request = new Request.Builder().type(RequestType.LOGIN).data(loginData).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            closeConnection();
            throw new MotorcyclesException((String) response.data());
        }
        this.client = client;
        return response.type() == ResponseType.OK;
    }

    @Override
    public User findAfterUsername(String username) throws MotorcyclesException {
        initializeConnection();
        Request request = new Request.Builder().type(RequestType.FIND_AFTER_USERNAME).data(username).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            closeConnection();
            throw new MotorcyclesException((String) response.data());
        }
        return (User) response.data();
    }

    @Override
    public void addUser(User user) throws MotorcyclesException {
        initializeConnection();
        Request request = new Request.Builder().type(RequestType.ADD_USER).data(user).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            closeConnection();
            throw new MotorcyclesException((String) response.data());
        }
    }

    @Override
    public String hashPassword(String password) throws MotorcyclesException {
        initializeConnection();
        Request request = new Request.Builder().type(RequestType.HASH_PASSWORD).data(password).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            closeConnection();
            throw new MotorcyclesException((String) response.data());
        }
        return (String) response.data();
    }


    @Override
    public long getNextParticipantId() throws MotorcyclesException {
        initializeConnection();
        Request request = new Request.Builder().type(RequestType.GET_NEXT_PARTICIPANT_ID).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            closeConnection();
            throw new MotorcyclesException((String) response.data());
        }
        return (long) response.data();
    }

    @Override
    public boolean isParticipantRegisteredForRace(Participant participant, Race race) throws MotorcyclesException {
        initializeConnection();
        Map<String, Object> registrationData = new HashMap<>();
        registrationData.put("participant", participant);
        registrationData.put("race", race);
        Request request = new Request.Builder().type(RequestType.IS_PARTICIPANT_REGISTERED_FOR_RACE).data(registrationData).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            closeConnection();
            throw new MotorcyclesException((String) response.data());
        }
        return (boolean) response.data();
    }

    private void closeConnection() {
        finished=true;
        try {
            input.close();
            output.close();
            connection.close();
            client = null;
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    private void sendRequest(Request request) throws MotorcyclesException {
        try {
            output.writeObject(request);
            output.flush();
        } catch (IOException e) {
            throw new MotorcyclesException("Error sending object "+e);
        }

    }

    private Response readResponse() throws MotorcyclesException {
        Response response=null;
        try{

            response=qresponses.take();

        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return response;
    }

    private void initializeConnection() throws MotorcyclesException {
        try {
            connection=new Socket(host,port);
            output=new ObjectOutputStream(connection.getOutputStream());
            output.flush();
            input=new ObjectInputStream(connection.getInputStream());
            finished=false;
            startReader();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void startReader(){
        Thread tw=new Thread(new ReaderThread());
        tw.start();
    }

    private void handleUpdate(Response response){
        if (response.type() == ResponseType.ADDED_RACE) {
            Race race = (Race) response.data();
            try {
                client.raceAdded(race);
            } catch (MotorcyclesException e) {
                e.printStackTrace();
            }
        }
    }



    private boolean isUpdate(Response response){
        return response.type()== ResponseType.ADDED_RACE ;
    }


    private class ReaderThread implements Runnable{
        public void run() {
            while(!finished){
                try {
                    Object response=input.readObject();
                    System.out.println("response received "+response);
                    if (isUpdate((Response)response)){
                        handleUpdate((Response)response);
                    }else{

                        try {
                            qresponses.put((Response)response);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                } catch (IOException e) {
                    System.out.println("Reading error "+e);
                } catch (ClassNotFoundException e) {
                    System.out.println("Reading error "+e);
                }
            }
        }
    }
}
