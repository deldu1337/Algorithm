import java.io.*;

public class Main_1541 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        String S[] = str.split("-");
        int sum = 0;
        for(int i=0;i<S.length;i++) {
            if(S[i].contains("+")) {
                String A[] = S[i].split("[+]");
                for(int j=0;j<A.length;j++) {
                    sum += Integer.parseInt(A[j]);
                }
                S[i] = String.valueOf(sum);
            }
            sum = 0;
        }

        sum = Integer.parseInt(S[0]);
        for(int i=1;i<S.length;i++) {
            sum -= Integer.parseInt(S[i]);
        }
        System.out.print(sum);

        bw.flush();
        bw.close();
        br.close();
    }
}