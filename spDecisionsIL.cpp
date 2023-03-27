/**
 *******************************************************************************
 * @file    spDecisionsIL.cpp
 * @brief   creating a program which finds the input number is even or odd and
 *          Writing a code that will get a single score from the user via the 
 *          keyboard then display a message to indicate whether the score meets
 *          the diving scoring requirements or not.
 *
 * @remarks
 *      Course:        Computer Science 2114, spring 2023
 *      Due Date:      Thursday, Feb 16 
 *      Instructor:    Ms. Draganjac
 *
 * @author  Swarnim Kathayat
 * @date    Thursday, Feb 16
 *******************************************************************************
**/

#include <iostream>
    using std:: cin;
    using std:: cout;
    using std:: endl;

int main()
{
    int num;
    cout << "\nEnter an integer: ";
    cin >> num;
    if (num % 2 == 0)
        cout << num << " is an even number.\n";
    else
        cout << num << " is an odd number.\n";


    //question number 2
    double diving_score;
    cout << "\nEnter diving score:  ";
    cin >> diving_score;
    if (diving_score >= 0 && diving_score <= 10) //checking if the number is between 0 and 10
    {
        int new_diving_score, div_score;
        new_diving_score = diving_score * 10; 
        div_score = new_diving_score % 10;
        if (div_score >= 0 && div_score <= 5)  //checking if the reminder falls between 0 and 5
        {
            cout << diving_score <<" is a valid diving score.";  // if yes
        }
        else
            cout << diving_score <<" is not a valid diving score."; // if n0
    }
    else
    cout << diving_score <<" is not a valid diving score.";
    cout << "\n";
    return 0;
}