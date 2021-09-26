// A Java program for a ClientSide
import java.net.*;
import java.io.*;
public class ClientProgram
{
// initialize socket and input output streams
	private Socket socket = null;
	private DataInputStream input = null;
	private DataOutputStream out = null;

// constructor to put ip address and port
	public void Client(String address, int port){
// establish a connection
	try {
		socket = new Socket(address, port);
		System.out.println("Connected to server - pipe open");

	// takes input from terminal
	input = new DataInputStream(System.in);
	// sends output to the socket
	out = new DataOutputStream(socket.getOutputStream());
}
	catch(UnknownHostException u){
		System.out.println(u);
}
	catch(IOException i){
		System.out.println(i + "Connection Refused - Server may be down - Tra agin later");
}	// string to read message from input
	String line = "";

	// keep reading until "Over" is inputted by the user
	while (!line.equals("Over")){
		try {
			line = input.readLine();
			out.writeUTF(line);
}
		catch(IOException i){
			System.out.println(i);
}
}
	// close the connection
		try{
			input.close();
			out.close();
			socket.close();
			System.out.println("Bye - Connection Terminated");
}
		catch(IOException i){
			System.out.println(i);
}
}
	public static void main(String args[]) {
	ClientProgram c = new ClientProgram();
	c.Client("127.0.0.1", 1735);
}
}