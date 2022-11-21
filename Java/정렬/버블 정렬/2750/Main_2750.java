import java.io.*;
import java.util.StringTokenizer;

public class Main_2750 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        int N = Integer.parseInt(st.nextToken());

        int A[] = new int[N];
        for(int i=0;i<N;i++) {
            String str1 = br.readLine();
            StringTokenizer st1 = new StringTokenizer(str1);
            A[i] = Integer.parseInt(st1.nextToken());
        }

        int tmp;
        for(int i=1;i<N;i++) {
            for(int j=1;j<N;j++) {
                if(A[j-1]>A[j]) {
                    tmp = A[j-1];
                    A[j-1] = A[j];
                    A[j] = tmp;
                }
            }
        }

        for(int i=0;i<N;i++) {
            bw.write(String.valueOf(A[i]));
            bw.newLine();
        }

        bw.flush();
        bw.close();
        br.close();
    }
}