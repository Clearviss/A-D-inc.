using System;

public class Class1
{
    public string id;
	public string name;
	public int age;
    public bool licencja;
    public double srednia;

    public Class1(string Aid, string aName, int aAge, bool Alicense, double Asrednia)
    {
        Console.WriteLine("Generuje adriana "+id);   
        name = aName;
        age = aAge; 
        licencja = Alicense;
        srednia = Asrednia;
        id = Aid;
        Console.WriteLine("Wygenerowano!");
    }

    public bool pelniak()
    {
        if (age > 15)
        {
            return true;
        }
        return false;
    }
}
