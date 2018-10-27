//
//  main.cpp
//  lab5
//
//  Created by  Daria Firsova on 27/10/2018.
//  Copyright © 2018  Daria Firsova. All rights reserved.
//

#include <iostream>
#include <thread>
using namespace std;

void printing()
{
    cout<<"hello"<<endl;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    thread th1(printing);
    th1.join();
    return 0;
}
