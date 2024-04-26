using static System.Net.Mime.MediaTypeNames;
using System.Text.Json.Nodes;
using System.Text.Json;

// async void SetUpData()
//        {
//            var client = new HttpClient();
//            var request = new HttpRequestMessage
//            {
//                Method = HttpMethod.Get,
//                RequestUri = new Uri("http://127.0.0.1:8000/"),
//                Headers =
//            {
//                { "Host", "127.0.0.1:8000" }
//            },
//            };
//            using (var response = await client.SendAsync(request))
//            {
                 
//                response.EnsureSuccessStatusCode();
//                var body = await response.Content.ReadAsStringAsync();
//                JsonNode data = JsonObject.Parse(body);
//                GetData(data);
//            }
//        }
//namespace Final_Project.Data
//{

//    public class Test
//    {
//        public List<Pokemon> pokemons;

//        public Test()
//        {
//            pokemons = new List<Pokemon>();
//            SetUpData();
//        }

       

//        void GetData(JsonNode data)
//        {
//            Pokemon pokemon = new Pokemon();
//            pokemons = JsonSerializer.Deserialize<List<Pokemon>>(data);
//            //foreach (Pokemon p in pokemons)
//            //{
                 

//            //}
//        }
//    }
//}
