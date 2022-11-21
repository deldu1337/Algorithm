import java.io.*;
import java.util.*;

public class Main_1929 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str, " ");
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());
        int A[] = new int[end + 1];
        for(int i=2;i<=end;i++) {
            A[i] = i;
        }
        for(int i=2;i<=Math.sqrt(end);i++) {
            if(A[i]==0) {
                continue;
            }
            for(int j=i+i;j<=end;j=j+i) {
                A[j] = 0;
            }
        }
        for(int i=start;i<=end;i++) {
            if(A[i]!=0) {
                System.out.println(A[i]);
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}