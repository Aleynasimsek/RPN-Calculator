using System;
using System.Collections.Generic;
using System.IO;

namespace RPNCalculator
{
    // --- 1. SOYUT OPERATOR SINIFI VE ALT SINIFLAR ---
    public abstract class Operator
    {
        public abstract double Execute(double left, double right);
    }

    public class Adder : Operator
    {
        public override double Execute(double left, double right) => left + right;
    }

    public class Subtracter : Operator
    {
        public override double Execute(double left, double right) => left - right;
    }

    public class Multiplier : Operator
    {
        public override double Execute(double left, double right) => left * right;
    }

    public class Divider : Operator
    {
        public override double Execute(double left, double right)
        {
            if (right == 0) throw new DivideByZeroException("Sıfıra bölme hatası!");
            return left / right;
        }
    }

    // --- 2. STACK SINIFI ---
    public class Stack
    {
        private System.Collections.Generic.Stack<double> _stack = new System.Collections.Generic.Stack<double>();

        public void Push(double value) => _stack.Push(value);

        public double Pop()
        {
            if (_stack.Count == 0) throw new InvalidOperationException("Eksik operand hatası: Yığın boş.");
            return _stack.Pop();
        }

        public int Count => _stack.Count;
        
        public void Clear() => _stack.Clear();
    }

    // --- 3. GUI / ARAYÜZ SINIFI ---
    public class CalculatorGui
    {
        public string GetInput()
        {
            return Console.ReadLine();
        }

        public void ShowOutput(string message)
        {
            Console.WriteLine(message);
        }
    }

    // --- 4. ANA CALCULATOR SINIFI ---
    public class Calculator
    {
        private Stack _stack;
        private CalculatorGui _gui;

        public Calculator()
        {
            _stack = new Stack();
            _gui = new CalculatorGui();
        }

        public void Run()
        {
            try
            {
                string input = _gui.GetInput();
                if (string.IsNullOrWhiteSpace(input)) return;

                string[] tokens = input.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);

                foreach (string token in tokens)
                {
                    if (double.TryParse(token, out double number))
                    {
                        _stack.Push(number);
                    }
                    else
                    {
                        Operator op = GetOperator(token);
                        if (op != null)
                        {
                            if (_stack.Count < 2) throw new InvalidOperationException("Eksik operand hatası!");
                            
                            double right = _stack.Pop();
                            double left = _stack.Pop();
                            
                            double result = op.Execute(left, right);
                            _stack.Push(result);
                        }
                        else
                        {
                            throw new ArgumentException($"Tanımsız operatör: {token}");
                        }
                    }
                }

                if (_stack.Count == 1)
                {
                    _gui.ShowOutput(_stack.Pop().ToString());
                }
                else if (_stack.Count > 1)
                {
                    throw new InvalidOperationException("Fazla operand/eksik operatör hatası!");
                }
            }
            catch (Exception ex)
            {
                LogException(ex);
                _gui.ShowOutput("HATA: " + ex.Message);
            }
        }

        private Operator GetOperator(string token)
        {
            switch (token)
            {
                case "+": return new Adder();
                case "-": return new Subtracter();
                case "*": return new Multiplier();
                case "/": return new Divider();
                case "x": return new Multiplier();
                default: return null;
            }
        }

        private void LogException(Exception ex)
        {
            try
            {
                File.AppendAllText("error_log.txt", DateTime.Now + ": " + ex.Message + "\n");
            }
            catch { }
        }

        public static void Main(string[] args)
        {
            Calculator app = new Calculator();
            app.Run();
        }
    }
}
