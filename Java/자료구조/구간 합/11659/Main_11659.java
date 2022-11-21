import java.io.*;
import java.util.StringTokenizer;

public class Main_11659 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str," ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int []A = new int[N+1];
        int []S = new int[N+1];
        A[0] = 0;
        S[0] = 0;

        String str1 = br.readLine();
        StringTokenizer st1 = new StringTokenizer(str1," ");

        for(int i=1;i<=N;i++) {
            A[i] = Integer.parseInt(st1.nextToken());
            S[i] = S[i-1] + A[i];
        }

        for(int k=0;k<M;k++) {
            String str2 = br.readLine();
            StringTokenizer st2 = new StringTokenizer(str2," ");
            int i = Integer.parseInt(st2.nextToken());
            int j = Integer.parseInt(st2.nextToken());

            bw.write(String.valueOf(S[j] - S[i-1]));
            if(k!=M-1)
                bw.newLine();
        }

        bw.flush();
        br.close();
        bw.close();
    }
}