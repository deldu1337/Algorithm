import java.io.*;
import java.util.*;

public class Main_1260 {

    static ArrayList<Integer>[] A;
    static Boolean visited[];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str, " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());

        A = new ArrayList[N+1];
        visited = new Boolean[N+1];
        for(int i=1;i<N+1;i++) {
            A[i] = new ArrayList<Integer>();
            visited[i] = false;
        }

        for(int i=0;i<M;i++) {
            String str1 = br.readLine();
            StringTokenizer st1 = new StringTokenizer(str1, " ");
            int s = Integer.parseInt(st1.nextToken());
            int e = Integer.parseInt(st1.nextToken());

            A[s].add(e);
            A[e].add(s);
        }
        for(int i=1;i<N+1;i++) {
            Collections.sort(A[i]);
        }

        DFS(V);
        System.out.println();
        visited = new Boolean[N+1];
        for(int i=1;i<N+1;i++) {
            visited[i] = false;
        }
        BFS(V);

        bw.flush();
        bw.close();
        br.close();
    }
    static void DFS(int v) {
        if(visited[v]) {
            return;
        }
        visited[v] = true;
        System.out.print(v + " ");
        for(int i : A[v]) {
            if(visited[i] == false) {
                DFS(i);
            }
        }
    }
    static void BFS(int v) {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(v);
        visited[v] = true;

        while(!queue.isEmpty()) {
            int now = queue.poll();
            System.out.print(now + " ");
            for(int i : A[now]) {
                if(!visited[i]) {
                    visited[i] = true;
                    queue.add(i);
                }
            }
        }
    }

}