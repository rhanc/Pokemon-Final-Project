using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final_Project.Data
{
    public class Moves
    {
        //public string[] moves { get; set; }
        public string name { get; set; }
        public string type { get; set; }
        public int power { get; set; } 
        public string effect { get; set; }

        public string GetData()
        {
            if (power!= 0)
            {
                return "Name: " + name + " Type: " + type + " Power: " + power + " "+effect;
            }
            else
            {
                return "Name: " + name + " Type: " + type + " Effect: "+effect;
            }
        } 
    }
}
