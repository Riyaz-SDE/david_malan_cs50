#include <stdio.h>
#include <string.h>
typedef struct 
{
    char employeeName[50];
    char EmpID[4];
    int salary;
    char phoneNumber[14];

} phoneBook;

int main(){
    phoneBook EmployeesDetails[3] = {
        [0] = {.employeeName = "riyaz", .EmpID = "0001", .salary = 17000, .phoneNumber = "+91-9176071968" },
       [1] = {.employeeName = "riyaz2", .EmpID = "0002", .salary = 18000, .phoneNumber = "+91-9176071969" },
        [2] = {.employeeName = "riyaz3", .EmpID = "0003", .salary = 19000, .phoneNumber = "+91-9176071960" }
    };
    int arrayLen = sizeof(EmployeesDetails)/sizeof(phoneBook);
    char serachName[20];
    scanf("%s", serachName);
    for(int i = 0; i < arrayLen; i++){
        if(strcmp(serachName,EmployeesDetails[i].employeeName) == 0){
            printf("Employee id %s\nEmployee salary %d\nEmployee mobile Number %s\n",
            EmployeesDetails[i].EmpID,EmployeesDetails[i].salary,EmployeesDetails[i].phoneNumber);
            return 0;
        }
    }
    printf("emp records not found ");
    // printf("%d",);
}
