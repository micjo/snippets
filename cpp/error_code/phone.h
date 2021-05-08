#ifndef COMMAND_H
#define COMMAND_H

#include <system_error>

namespace micjo {

class Strategy {
public:
  virtual void execute() = 0;
  virtual std::error_code popError() = 0;
  virtual std::error_code peekError() = 0;
  virtual ~Strategy() = default;
};

class MakePhoneCall : public Strategy {
public:
  MakePhoneCall() = default;
  void execute() override;
  std::error_code popError() override;
  std::error_code peekError() override;

private:
  std::error_code _errc;
};

} // namespace micjo

#endif // COMMAND_H
