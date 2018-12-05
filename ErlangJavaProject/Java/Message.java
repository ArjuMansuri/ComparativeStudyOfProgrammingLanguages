class Message {
   
	public synchronized void intro(String sender,String receiver,Long time) {
	
     System.out.println(receiver+" received intro message from "+sender+" ["+time+"]");
   
   }

   public synchronized void reply(String receiver,String sender,Long time) {
      
      System.out.println(sender+" received reply message from "+receiver+" ["+time+"]");
    }
   
   
}
