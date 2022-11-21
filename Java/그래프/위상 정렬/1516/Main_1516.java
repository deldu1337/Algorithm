import java.io.*;
import java.util.*;

public class Main_1516 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        int N = Integer.parseInt(st.nextToken());
        ArrayList<ArrayList<Integer>> A = new ArrayList<>();
        for(int i=0;i<=N;i++) {
            A.add(new ArrayList<>());
        }
        int[] indegree = new int[N+1];
        int[] selfBuild = new int[N+1];
        for(int i=1;i<=N;i++) {
            str = br.readLine();
            st = new StringTokenizer(str, " ");
            selfBuild[i] = Integer.parseInt(st.nextToken());
            while (true) {
                int preTmp = Integer.parseInt(st.nextToken());
                if (preTmp == -1) {
                    break;
                }
                A.get(preTmp).add(i);
                indegree[i]++;
            }
        }
        Queue<Integer> queue = new LinkedList<>();
        for(int i=1;i<=N;i++) {
            if(indegree[i] == 0) {
                queue.offer(i);
            }
        }
        int[] result = new int[N+1];
        while(!queue.isEmpty()) {
            int now = queue.poll();
            for(int next: A.get(now)) {
                indegree[next]--;
                result[next] = Math.max(result[next], result[now] + selfBuild[now]);
                if(indegree[next] == 0) {
                    queue.offer(next);
                }
            }
        }
        for(int i=1;i<=N;i++) {
            System.out.println(result[i] + selfBuild[i]);
        }

        bw.flush();
        bw.close();
        br.close();
    }

}