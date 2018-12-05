import java.util.ArrayList;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;


public class SenderProcess implements Runnable{
	private Thread t;
	private Row row;
	BlockingQueue<String> bQ=new LinkedBlockingQueue<String>();
	Message m=new Message();

	public Thread getT() {
		return t;
	}

	public void setT(Thread t) {
		this.t = t;
	}
	
	public SenderProcess(Row row) {
		super();
		this.row = row;
	}

	public void start(){
		if(t==null){
			t=new Thread(this, row.getSender());
			t.start();
		}
	}
	
	public void end(ArrayList<String> list) throws InterruptedException{
		   synchronized (list) {
			if(Exchange.count < Exchange.size-1){
			++Exchange.count;
			try {
				list.wait();
			} catch (InterruptedException e) {
				e.printStackTrace();
			} 
		   }else{
		   
			   list.notifyAll();
		   }
		   } 
		   System.out.println("\nProcess "+ Thread.currentThread().getName() +" has received no calls for 1 second, ending...");
		   if(Exchange.count == Exchange.size-1){
				Exchange.count++;
				if(Exchange.count == Exchange.size){
					Thread.sleep(1500);
				   System.out.println("\nMaster has received no calls for 1.5 seconds, ending...");  
				}
			}
		   
	   }
	
	@Override
	public void run() {
		
		for (String receiver : row.getReceivers()) {
			try {
			getT().sleep((long)(Math.random() * 1000)); 
			Long t=System.currentTimeMillis();
			
			m.intro(row.getSender(),receiver,t);
			
				getT().sleep((long)(Math.random() * 1000)); 
				m.reply(receiver, row.getSender(),t);
				//m.end(sender);
				
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			
		}
		try {
			getT().sleep((long)(Math.random() * 1000));
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
			
		
		try {
			this.end(MasterProcess.list);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
				
	}
}
