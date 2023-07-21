import java.util.HashMap;
public class Hash {

    Hash(){


    }
    public static void main(String[] args) {
    HashMap<String, String> capitalCities;
    HashMap<String, String> dict;
    capitalCities = new HashMap<>();
    dict = new HashMap<>();
    dict.put("brand", "ford");
    dict.put("model", "mustang");
    dict.put("year", "1964");
    capitalCities.put("England","London");
    capitalCities.put("Germany","Berlin");
    capitalCities.put("Norway","Oslo");
    System.out.println(dict);
    System.out.println(capitalCities);
    }
}
