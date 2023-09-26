double inC = 0;
double all = 50000000;
var rand = new Random();
double xCoord;
double yCoord;
for (int i = 0; i < all; i++)
{
    xCoord = rand.NextDouble();
    yCoord = rand.NextDouble();
    if (Math.Sqrt(Math.Pow(xCoord - 0.5,2)  + Math.Pow(yCoord - 0.5,2)) <= 0.5)
    {
        inC++;
    }
}
Console.WriteLine((inC * 4) / all);