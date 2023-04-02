namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("podaj liczbe limit 100000");
            string input = Console.ReadLine();
            int liczba;
            int reszta = 0;
            while (true)
            {
                if (int.TryParse(input, out liczba))
                {
                    if (liczba > 100000)
                    {
                        Console.WriteLine("podales za duza liczbe");
                        break;
                    }
                    for (int i = 1; i <= liczba; i = i * 2)
                    {
                        Console.WriteLine(i);
                        if (i == liczba)
                        {
                            Console.WriteLine("Program sie zakonczyl");
                        }
                        reszta = liczba - i;
                    }
                    
                    Console.WriteLine("liczby wypisane, dopisz kolejne reszta: ");
                    Console.WriteLine(reszta);
                    input = Console.ReadLine();
                }
                else
                {
                    Console.WriteLine("podales ciag znakow!");
                    break;
                }
            }
           
            
            
            
        }
    }
}