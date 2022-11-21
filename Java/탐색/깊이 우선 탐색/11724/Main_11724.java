import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main_11724 {

    static ArrayList<Integer>[] A;
    static Boolean visited[];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str, " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        A = new ArrayList[N+1];
        visited = new Boolean[N+1];
        for(int i=1;i<N+1;i++) {
            A[i] = new ArrayList<Integer>();
            visited[i] = false;
        }

        String str1;
        StringTokenizer st1;
        for(int i=0;i<M;i++) {
            str1 = br.readLine();
            st1 = new StringTokenizer(str1, " ");
            int u = Integer.parseInt(st1.nextToken());
            int v = Integer.parseInt(st1.nextToken());

            A[u].add(v);
            A[v].add(u);
        }

        int cnt = 0;
        for(int i=1;i<N+1;i++) {
            if(!visited[i]) {
                cnt++;
                DFS(i);
            }
        }
        bw.write(String.valueOf(cnt));

        bw.flush();
        bw.close();
        br.close();
    }
    static void DFS(int v) {
        if(visited[v]) {
            return;
        }
        visited[v] = true;
        for(int i : A[v]) {
            if(visited[i] == false) {
                DFS(i);
            }
        }
    }
}