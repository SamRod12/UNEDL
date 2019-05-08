using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace delegates
{
    public delegate void valores(Double x, Double y);

    class delagate {
        static void Main(String[] artgs) {
            
            Double x, y;
            
            x = Convert.ToSingle(Console.ReadLine());
            y = Convert.ToSingle(Console.ReadLine());
            valores val = new valores(operaciones.suma);
            val(x,y);
            val = new valores(operaciones.res);
            val(x, y);
            val = new valores(operaciones.mul);
            val(x, y);
            val = new valores(operaciones.div);
            val(x, y);
        }



        class  operaciones{
            public static void suma(Double x, Double y) {

               Console.WriteLine("resultado de suma es:   "+ (x + y));
            }
            public static void res(Double x, Double y)
            {
            
                Console.WriteLine("resultado de la resta es:   " + (x - y));
            }
            public static void mul(Double x, Double y)
            {

                Console.WriteLine("resultado de multipiplicacion es:    " + (x * y));
            }
            public static void div(Double x, Double y)
            { 
                Console.WriteLine("resultado de la division es:      " + (x / y));
            }

        }

    }




    }
