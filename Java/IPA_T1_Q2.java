import java.util.*;

public class IPA_T1_Q2 {
    public static class Player{
        int playerId;
        String playerName;
        int runs;
        String playerType;
        String matchType;

        public Player(){}
        //setters
        public void setId(int i){ playerId = i;}
        public void setName (String n){ playerName = n; }
        public void setRuns (int r) { runs = r;}
        public void setPType (String s) { playerType = s; }
        public void setMtype (String s) { matchType = s; }
        //getters
        public int getId(){ return playerId; }
        public int getRuns() { return runs; }
        public String getPType() { return playerType; }
        public String getMType() { return matchType; }

        public void display()
        {
            System.out.println("ID: "+playerId);
            System.out.println("Name: "+playerName);
            System.out.println("Runs: "+runs);
            System.out.println("Player Type: "+playerType);
            System.out.println("Match Type: "+matchType);
        }
    }      

    public static void findPlayerWithLowestRuns(Player p[], String s){
        int count=0, r[] = new int[4];
        for(int i=0;i<4;i++)
        {
            if(s.equals(p[i].getPType()))
            {
                r[count] = p[i].getRuns();
            }
        }
        if(r.length==0)
            System.out.println("No such player");
        else{
            Arrays.sort(r);
            System.out.println(r[0]);
        }
    }

    public static void findPlayerByMatchType(Player p[], String s){
        int count=0, r[] = new int[4];
        for(int i=0;i<4;i++)
        {
            if(s.equals(p[i].getMType()))
            {
                r[count] = p[i].getId();
            }
        }
        if(r.length==0){
            System.out.println("No with match type");
        }
        else{
            for(int i=0;i<r.length;i++)
            {
                System.out.println(r[i]);
            }
        }
    }
    public static void main(String[] args)
    {
        int i;
        Player p[] = new Player[4];
        try(Scanner ip = new Scanner (System.in);)
        {
            for (i=0; i<1; i++)
            {
                p[i] = new Player();
                p[i].setId(ip.nextInt());
                ip.nextLine();
                p[i].setName(ip.nextLine());
                p[i].setRuns(ip.nextInt());

                ip.nextLine();
                p[i].setPType(ip.nextLine());
                p[i].setMtype(ip.nextLine());
                //System.out.println("yo");
            }
            
            p[0].display();
            
            
            //String Ptype = ip.nextLine();
            //String Mtype = ip.nextLine();

            //findPlayerWithLowestRuns(p, Ptype);
            //findPlayerByMatchType(p, Mtype);
        }
    }   
}