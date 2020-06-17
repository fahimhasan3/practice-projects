using System;

namespace ConsoleGame
{
    class Game : SuperGame
    {
        public new static void UpdatePosition(string key, out int xChange, out int yChange)
        {
            key = key.ToLower();
            yChange = 0;
            xChange = 0;
            switch (key)
            {
                case "leftarrow":
                    xChange = -1;
                    break;
                case "rightarrow":
                    xChange = 1;
                    break;
                case "downarrow":
                    yChange = 1;
                    break;
                case "uparrow":
                    yChange = -1;
                    break;
                default:
                    break;
            }
        }

        public new static char UpdateCursor(string key)
        {
            key = key.ToLower();
            char symbol = '<';
            switch (key)
            {
                case "leftarrow":
                    symbol = '<';
                    break;
                case "rightarrow":
                    symbol = '>';
                    break;
                case "downarrow":
                    symbol = 'v';
                    break;
                case "uparrow":
                    symbol = '^';
                    break;
                default:
                    symbol = '<';
                    break;
            }
            return symbol;

        }

        public new static int KeepInBounds(int dimension, int max)
        {
            int newDimension;
            if (dimension >= max)
            {
                newDimension = max - 1;
            }
            else if (dimension < 0)
            {
                newDimension = 0;
            }
            else
            {
                newDimension = dimension;
            }
            return newDimension;
        }

        public new static bool DidScore(int x1, int y1, int x2, int y2)
        {
            if (x1 == x2 && y1 == y2)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}