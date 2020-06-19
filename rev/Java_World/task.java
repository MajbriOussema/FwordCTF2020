import java.time.Instant;
import java.text.*; 
import java.util.*;
import java.util.function.*;
import java.lang.Math;

public class task{
    public static final int LENGTH = 36;
    public static String password = "FwordCTF{Y_d0es_3veRy_1_h4t3_j4Va_?}";
    public static String gen(Collator coll){
        Random rand = new Random();
        Instant now = Instant.now();
        long seed = now.getEpochSecond();
        rand.setSeed(seed);
        int i;
        String longkey = "";
        for(i=0;i<(36+seed%10);i++){
            longkey += (char)(97+rand.nextInt(25));
        }
        System.out.println("longkey = "+longkey);
        coll.setStrength((int)seed%4);
        return longkey;
    }
    public static int trash(int x){
        int i,j;
        String xx = Integer.toBinaryString(x),res="";
        for(i=0;i<xx.length();i++){
            res += xx.charAt(i) == '0' ? '1' : '0';
        }
        return Integer.parseInt(res, 2);
    }
    public static int[][] hide(String longkey){
        int i,j,x;
        String res="";
        int [] tab = new int[LENGTH];
        int [][] hidden = new int[9][8];
        for(i=(LENGTH/2 -1);i>=0;i--){
            tab[i] = (int)flag.charAt(i) ^ (160 >> (2 & 10));
        }   
        for(i=(LENGTH/2);i<LENGTH;i++){
            x = (int)flag.charAt(i);
            tab[i] = (x | 4 ) & (~x | (-110 >> 5));
        }

        for(j=0,i=(longkey.length()-1);j<LENGTH && i>=0;i--,j++){
            res += i % 4 != 0 ? (char)((int)longkey.charAt(i % 4)  + (int)tab[j] - 100): (char)(((int)tab[j] ^ (int)longkey.charAt(j % 5) ));
            res += i % 2 == 0 ? longkey.charAt(j % 5) : longkey.charAt(i % 4);
        }
        int k = 0;
        for(i=0;i<9;i++){
            for(j=0;j<8;j++){
                hidden[i][j] = (int)res.charAt(k++);
            }
        }
        System.out.println(res);
        return hidden;
    }
    public static void read_input(String input,int key){
        Scanner scan = new Scanner(System.in);
        System.out.println("-!- Welcome to the world of JAVA -!-");
        System.out.println("-!- I'm going to ask you about something, let's talk later about the flag -!-");
        
        try {
            System.out.println("-?- What's your favorite number ? -?-");
            System.out.print(">>");
            key = scan.nextInt();
            System.out.println("-?- Can you tell me the secret to get the flag ? -?-");
            System.out.print(">>");
            scan.nextLine();
            input = scan.nextLine();
        }
        catch(Exception e){
            System.out.println("/!\\ Something is wrong, try later please /!\\");
        }
    }
    public static String reverse(String ciphertext){
        String plaintext = "";
        return plaintext;
    }
    public static void main(String [] args){
        String longkey,input = "";
        int [][] hidden = new int [9][8];
        int key = 0;
        Collator myCollator = Collator.getInstance(Locale.US);
        longkey = gen(myCollator);
        //System.out.println(myCollator.getStrength());
        hidden = hide(longkey);
        for(int i=0;i<9;i++){
            for(int k=0;k<8;k++){
                System.out.print(hidden[i][k]+" ");
            }
            System.out.println();
        }
        if((myCollator.compare(longkey , longkey.toUpperCase()))==0){
            System.out.println(hidden);
        }
        //read_input(input,key);
        
    }
}