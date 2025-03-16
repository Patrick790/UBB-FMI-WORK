package com.network.utils;

import com.network.rpcprotocol.MotorcyclesClientRpcReflectionWorker;
import com.services.IMotorcyclesServices;

import java.net.Socket;

public class  MotorcyclesRpcConcurrentServer extends AbsConcurrentServer {

    private final IMotorcyclesServices motorcyclesServer;

    public MotorcyclesRpcConcurrentServer(int port, IMotorcyclesServices motorcyclesServer) {
        super(port);
        this.motorcyclesServer = motorcyclesServer;
        System.out.println("Motorcycles- MotorcyclesRpcConcurrentServer");
    }
    @Override
    protected Thread createWorker(Socket client) {
        MotorcyclesClientRpcReflectionWorker worker = new MotorcyclesClientRpcReflectionWorker(motorcyclesServer, client);
        return new Thread(worker);
    }

    @Override
    public void stop(){
        System.out.println("Stopping services ...");
    }
}
