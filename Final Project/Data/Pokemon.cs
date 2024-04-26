using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final_Project.Data
{
    public class Pokemon
    {
        public int id { get; set; }
        public string name { get ; set; }
        public string[] types { get; set ; }
        public string[] weaknesses { get; set; }
        public string ImageUrl;
        //public Moves[] moves { get; set; }
        public Moves[] moves { get; set; }
        public Pokemon()
        { 
            types = new string[10];
            weaknesses = new string[10];
            //moves = new Moves[10];
            moves =  new Moves[10];
            for (int i = 0; i < moves.Length; i++)
            {
                moves[i] = new Moves();
            }
        }

        public override string ToString()
        {
            string type = "";
            foreach (string t in types)
            {
                type += t + " ";
            }
            string weaks = "";
            foreach (string w in weaknesses)
            {
                weaks += w+" ";
            }
            string move = "\n";
            for (int i = 0; i < moves.Length; i++)
            {
                move += moves[i].GetData() + "\n";
            }
            return "Name: "+name + "\nTypes: " + type + "\nWeaknesses: " + weaks + "\nMoves: " + move;
        }
    }
}
