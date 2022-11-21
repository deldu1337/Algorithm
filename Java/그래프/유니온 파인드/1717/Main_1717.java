import java.io.*;
import java.util.*;

public class Main_1717 {

    public static int[] parent;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str, " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        parent = new int[n+1];
        for(int i=0;i<=n;i++) {
            parent[i] = i;
        }
        for(int i=0;i<m;i++) {
            str = br.readLine();
            st = new StringTokenizer(str, " ");
            int question = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if(question == 0) {
                union(a, b);
            } else {
                if(checkSame(a, b)) {
                    System.out.println("YES");
                } else {
                    System.out.println("NO");
                }
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
    public static void union(int a, int b) {
        a = find(a);
        b = find(b);
        if(a != b) {
            parent[b] = a;
        }
    }
    public static int find(int a) {
        if(a == parent[a]) {
            return a;
        } else {
            return parent[a] = find(parent[a]);
        }
    }
    public static boolean checkSame(int a, int b) {
        a = find(a);
        b = find(b);
        if(a == b) {
            return true;
        }
        return false;
    }
}