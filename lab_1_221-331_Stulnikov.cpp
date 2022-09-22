// lab_1_221-331_Stulnikov.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <bitset>
#include <float.h>
using namespace std;

int main()
{
	
	setlocale(LC_ALL, "Rus");
	cout << "Задание №1" << "\n" << "\n";
	cout << "Стульников Сергей Андреевич, 221-331" << endl << "\n";

	cout << "Задание №2" << "\n" << "\n";
	cout <<"min int = "<< int(0b10000000000000000000000000000000) << ", max int = " << int(0b01111111111111111111111111111111) << ", size of int = " << sizeof(int) << "\n";
   cout << "min unsigned int = " << unsigned int(0b00000000000000000000000000000000) << ", max unsigne int = " << unsigned int(0b11111111111111111111111111111111) << ", size of int = " << sizeof(unsigned int) << "\n";
   cout << "min short = " << short(0b1000000000000000) << ", max short = " << short(0b0111111111111111) << ", size of short = " << sizeof(short) << "\n";
   cout << "min unsigned short = " << unsigned short(0b000000000000000) << ", max unsigned short = " << unsigned short(0b1111111111111111) << ", size of unsigned short = " << sizeof(unsigned short) << "\n";
   cout << "min long = " << long(0b10000000000000000000000000000000) << ", max long = " << long(0b01111111111111111111111111111111) << ", size of long = " << sizeof(long) << "\n";
   cout << "min long long = " << long long(0b1000000000000000000000000000000000000000000000000000000000000000) << ", max long long = " << long long(0b0111111111111111111111111111111111111111111111111111111111111111) << ", size of long long = " << sizeof(long long) << "\n";
   cout << "min double = " << double(-DBL_MAX) << ", max double = " << double(DBL_MAX) << ", size of double = " << sizeof(double) << "\n";
   cout << "min char = " << char(0b00000000) << ", max char = " << char(0b11111111) << ", size of char = " << sizeof(char) << "\n";
   cout << "min bool = " << bool(0b00000000) << ", max bool = " << bool(0b11111111) << ", size of bool = " << sizeof(bool) << "\n" <<"\n";

   cout << "Задание №3" << "\n" << "\n";
   cout << "Введите число:" << "\n";
   int number;
   cin >>  number;
   cout << "В бинарном виде: " << bitset<sizeof(number) * 8>(number) << "\n";
   cout << "В шестнадцатиричном виде:" << hex << number << "\n";
   bool boolnum = number;
   double doublenum = number;
   char charnum = number;
   cout << "bool = " << boolnum << "\n";
   cout << "double = " << doublenum << "\n";
   cout << "char = " <<charnum << "\n" << "\n";
   
   cout << "Задание №4" << "\n" << "\n";
   cout << "Введите коэффициенты a * x = b:" << "\n";
   double a, b;
   cin >> a >> b;
   cout << a << " * x = " << b << "\n";
   cout << "x = " << b << " / " << a << "\n";
   cout << "x = " << b / a << "\n" << "\n";

   cout << "Задание №5" << "\n" << "\n";
   cout << "Введите координаты отрезка на прямой:" << "\n";
   int x, y;
   cin >> x >> y;
   cout << "Середина отрезка находится в точке с координатой " << (x + y) / 2.;


   return 0;
}

// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
