import java.io.*;
import java.util.*;

public class Main_1920 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        int N = Integer.parseInt(st.nextToken());

        str = br.readLine();
        st = new StringTokenizer(str, " ");
        int A[] = new int[N];
        for(int i=0;i<N;i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);

        str = br.readLine();
        st = new StringTokenizer(str);
        int M = Integer.parseInt(st.nextToken());

        str = br.readLine();
        st = new StringTokenizer(str, " ");
        for(int i=0;i<M;i++) {
            int num = Integer.parseInt(st.nextToken());
            int start = 0;
            int end = A.length - 1;
            Boolean find = false;
            while(start <= end) {
                int midi = (start + end) / 2;
                int midV = A[midi];
                if(midV > num) {
                    end = midi - 1;
                } else if(midV < num) {
                    start = midi + 1;
                } else {
                    find = true;
                    break;
                }
            }
            if(find) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }


        bw.flush();
        bw.close();
        br.close();
    }
}