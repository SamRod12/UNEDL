using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RecorridoMatriz4x4
{
    class Program
    {
        static void Main(string[] args)
        {
            int[,] matriz = { { 1, 3, 5, 7 }, { 4, 7, 9, 7 }, { 2, 6, 8, 0 }, { 2, 4, 5, 2 } };
            
            int cont = 0;
           
            for (int o = 0; o < 4; o++)
            {
                for (int p = 0; p < 4; p++)
                {
                    Console.Write(matriz[o,p] + (","));
                }
                Console.WriteLine();
                
            }
            Console.WriteLine();
            for (int i = 0; i < 4; i++)
            {
                if (cont % 2 == 0)
                {
                    for (int abajo = 0; abajo < 4; abajo++)
                    {
                        Console.Write(matriz[abajo,cont] + (","));
                    }
                    cont++;
                }
                else if (cont % 2 == 1)
                {
                    for (int arriba = 4 - 1; arriba >= 0; arriba--)
                    {
                        Console.Write(matriz[arriba,cont] + (","));
                    }
                    cont++;
                }

            }
        }
    }
}
