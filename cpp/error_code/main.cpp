#include "phone.h"
#include <iostream>

int main(int /*argc*/, char ** /*argv[]*/) {

  micjo::MakePhoneCall callSomeone;

  callSomeone.execute();

  std::error_code errc = callSomeone.popError();

  if (errc) {
    std::cout << errc.message() << std::endl;
  }
}
