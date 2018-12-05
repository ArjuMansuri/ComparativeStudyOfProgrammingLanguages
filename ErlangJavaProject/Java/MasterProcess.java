import java.io.IOException;
import java.util.ArrayList;

public class MasterProcess implements Runnable {

	private Thread t;
	private String threadName;
	public static ArrayList<String> list = new ArrayList<>();
	public static int flag = 0;
	 
	public MasterProcess(String threadName) {
		super();
		this.threadName = threadName;
	}

	public Thread getT() {
		return t;
	}

	public void setT(Thread t) {
		this.t = t;
	}

	public String getThreadName() {
		return threadName;
	}

	public void setThreadName(String threadName) {
		this.threadName = threadName;
	}
	
	public void start(){
		if(t==null){
			t=new Thread(this, threadName);
			t.start();
		}
	}
	@Override
	public void run() {
		Exchange ex=new Exchange();
		try {
			ex.setContactsMap();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		for(Row row:ex.getContactsMap()){
			
			SenderProcess sp=new SenderProcess(row);
			sp.start();
			
			
		}
		
		
		
	}

}
