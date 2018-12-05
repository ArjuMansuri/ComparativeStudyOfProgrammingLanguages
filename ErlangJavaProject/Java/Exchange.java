import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Exchange {
	
	public static int count=0;
	public static int size;

	private ArrayList<Row> contactsMap=new ArrayList<>();
	
	
	public ArrayList<Row> getContactsMap() {
		return contactsMap;
	}


	public void setContactsMap(ArrayList<Row> contactsMap) {
		this.contactsMap = contactsMap;
	}


	public void setContactsMap() throws IOException {
		
		BufferedReader br = new BufferedReader(new FileReader("calls.txt"));
		String line="";
		
		while((line=br.readLine())!=null){
		
		
		String regx = ".{}[] ";
	    char[] ca = regx.toCharArray();
	    for (char c : ca) {
	   line=line.replace(""+c, "");
	  }
	   
	    String[] strArr=line.split(",");
	    ArrayList<String> recList=new ArrayList<>();
	    for (int i = 1; i < strArr.length; i++) {
	    	recList.add(strArr[i]);
		}
	    Row row=new Row(strArr[0], recList);
	   contactsMap.add(row);
	   
	}
		Exchange.size=getContactsMap().size();
		br.close();
	}

	public static void killer(){
		if(Exchange.count == Exchange.size-1){
			 Exchange.count++;
			if(Exchange.count == Exchange.size){
			   System.out.println("Master has received no replies for 1.5 seconds, ending...");  
			}
		}
	}

	public static void main(String[] args) throws IOException, InterruptedException {
		
	Exchange ex=new Exchange();
	ex.setContactsMap();
	
	System.out.println("** Calls to be made **");
	for(Row row:ex.getContactsMap()){
		
		StringBuffer menuRow=new StringBuffer(row.getSender());
		menuRow.append(": [");
		int count=0;
		for (String receiver: row.getReceivers()) {
			count++;
			menuRow.append(receiver);
			if(!(count==row.getReceivers().size())){
				menuRow.append(",");
			}
			
			
		}
		menuRow.append("]");
		System.out.println(menuRow);
	}
	System.out.println();
	MasterProcess mp=new MasterProcess("master");
	mp.start();
	Exchange.killer();
	}
}
