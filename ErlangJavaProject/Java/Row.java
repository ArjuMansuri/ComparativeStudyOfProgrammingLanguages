import java.util.ArrayList;

public class Row {

	private String sender;
	private ArrayList<String> receivers;
	
	public Row(String sender, ArrayList<String> receivers) {
		super();
		this.sender = sender;
		this.receivers = receivers;
	}
	
	public String getSender() {
		return sender;
	}
	public void setSender(String sender) {
		this.sender = sender;
	}
	public ArrayList<String> getReceivers() {
		return receivers;
	}
	
	public void setReceivers(ArrayList<String> receivers) {
		this.receivers = receivers;
	}
	
}
