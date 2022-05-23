using System.Collections.Generic;
using System.IO;
// See https://aka.ms/new-console-template for more information

//Get the input path
Console.WriteLine("please enter the path of your input files ");
string inputPath = Console.ReadLine();



//Get the output path
Console.WriteLine("please enter the path of your output files");
string outputPath = Console.ReadLine();



//create output directory
var Output = Directory.CreateDirectory(outputPath);



//read input directory and files
string[] inputDir = Directory.GetDirectories(inputPath);
string[] files = Directory.GetFiles(inputPath, "*.txt", SearchOption.AllDirectories);
List<string> results = files.ToList();



//create words and path dictionaries
IDictionary<string, List<int>> numberNames = new Dictionary<string, List<int>>();
IDictionary<string, int> fileNumber = new Dictionary<string, int>();



//put values in both dictionaries and reading the inputs context
foreach (string file in files)
{
    var specificNumber = fileNumber.Count;

    fileNumber.Add(Path.GetFullPath(file), specificNumber);

    var Text = File.ReadAllLines(file);

    foreach (var line in Text)
    {
        string[] words = line.Split(" ");

        foreach (string word in words)
        {
            if (numberNames.ContainsKey(word))
            {
                List<int> numbers = numberNames[word];
                if (!numbers.Contains(specificNumber))
                {
                    numbers.Add(specificNumber);
                }
            }
            else
            {
                List<int> values = new List<int>();
                values.Add(specificNumber);
                numberNames.Add(word, values);
            }
        }
    }
}



//reading the existing output files
string[] dicFilesArr = Directory.GetFiles(outputPath, "*.dic", SearchOption.AllDirectories);
List<string> dicFiles = new List<string>();



//find output files names
foreach (string file in dicFilesArr)
{
    var name = Path.GetFileName(file);
    dicFiles.Add(name);
}



//write all the words in their related file
foreach (var str in numberNames.Keys)
{

    if (str.Length >= 1)
    {
        var sbr = str.Substring(0, 1);
        char sbrChar = char.Parse(sbr);
        if (Char.IsLetter(sbrChar) == true && char.IsAscii(sbrChar) == true)
        {
            sbr = sbr.ToUpper();
            var dic = dicFiles.FirstOrDefault(x => x.Contains(sbr));
            var numberNamesArr = numberNames[str].ToArray();
            var dicLines = string.Join(" , ", numberNamesArr);

            if (dic == null)
            {
                using (StreamWriter writer = File.CreateText($"{outputPath}\\{sbr}.dic"))
                {
                    writer.WriteLine($"{str}  |  {dicLines} ");
                    var dicf = Path.GetFileName($"{outputPath}\\{sbr}.dic");
                    dicFiles.Add(dicf);
                }

            }
            else
            {
                using (StreamWriter sw = File.AppendText($"{outputPath}\\{sbr}.dic"))
                {
                    sw.WriteLine($"{str}  |  {dicLines} ");

                }
            }

        }
    }
}



// write the keys and values 
foreach (var st in numberNames.Keys.Where(x => numberNames[x].Count > 1))
{
    Console.WriteLine(st);
    foreach (int value in numberNames[st])
    {
        Console.WriteLine(value);
    }
}
Console.ReadKey();
