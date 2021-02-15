import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

public class playerAnalysis {

  public static void main(String[] args) throws IOException {

      String url = "https://www.espn.com/mlb/team/stats/_/name/cin/season/2002/seasontype/2";

      Document doc = Jsoup.connect(url).get();
      String title = doc.title();
      System.out.println(title);
  }
}
