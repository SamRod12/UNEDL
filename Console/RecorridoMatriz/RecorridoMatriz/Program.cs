using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RecorridoMatriz
{
    class Program
    {
        static void Main(string[] args)
        {
            int[,] matriz = new int [6,6]{{-9,-9,-9, 1, 1, 1},{ 0,-9, 0, 4, 3, 2},
                      {-9,-9,-9, 1, 2, 3},
                      { 0, 0, 8, 6, 6, 0},
                      { 0, 0, 0,-2, 0, 0},
                      { 0, 0, 1, 2, 4, 0}};

            int [,] resultado = new int[4,4];

            for (int filas = 0; filas < 4; filas++)
            {
                for (int columnas = 0; columnas < 4; columnas++)
                {

                    resultado[filas,columnas] = matriz[filas,columnas] + matriz[filas,columnas + 1] + matriz[filas,columnas + 2] + matriz[filas + 1,columnas + 1] + matriz[filas + 2,columnas] + matriz[filas + 2,columnas + 1] + matriz[filas + 2,columnas + 2];
                    Console.Write(resultado[filas,columnas]);
                    Console.Write(" ");
                }
                Console.WriteLine();
            }


        }
    }
}
