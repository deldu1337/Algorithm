import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_1253 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str, " ");
        int N = Integer.parseInt(st.nextToken());

        String str1 = br.readLine();
        StringTokenizer st1 = new StringTokenizer(str1, " ");
        int arr[] = new int[N];
        int result = 0;
        for(int i=0;i<N;i++) {
            arr[i] = Integer.parseInt(st1.nextToken());
        }
        Arrays.sort(arr);
        for(int k=0;k<N;k++) {
            int find = arr[k];
            int i=0;
            int j=N-1;

            while(i<j) {
                if(arr[i] + arr[j] == find) {
                    if(i != k && j != k) {
                        result++;
                        break;
                    } else if(i == k) {
                        i++;
                    } else if(j == k) {
                        j--;
                    }
                } else if(arr[i] + arr[j] < find) {
                    i++;
                } else {
                    j--;
                }
            }
        }
        System.out.print(result);

        bw.close();
        br.close();

    }
}