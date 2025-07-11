import java.util.HashSet;
import java.util.Set;

public class UniqueSetExample {
    public static void main(String[] args) {
        Set<Object> s = new HashSet<>();
        s.add(20);       // Integer
        s.add(20.0);     // Double
        s.add("20");     // String

        System.out.println("Size of set: " + s.size());  // Output: 3
    }
}
