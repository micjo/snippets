#include "phone.h"

enum class PhoneCallError {
  Ok = 0,
  InvalidNumber,
  NumberOccupied,
  OutOfCallingCredit
};

namespace std {
template <> struct is_error_code_enum<PhoneCallError> : public true_type {};
} // namespace std

namespace {
class PhoneErrorCategory : public std::error_category {
  const char *name() const noexcept override { return "PhoneCall"; }
  std::string message(int ev) const override {
    switch (static_cast<PhoneCallError>(ev)) {
    case PhoneCallError::InvalidNumber:
      return "[PhoneCall] Invalid number";
    case PhoneCallError::NumberOccupied:
      return "[PhoneCall] Number occupied";
    case PhoneCallError::OutOfCallingCredit:
      return "[PhoneCall] Out of calling credit";
    default:
      return "(Unrecognized error)";
    }
  }
} const phoneErrorCategory;

} // namespace

std::error_code make_error_code(PhoneCallError e) {
  return {static_cast<int>(e), phoneErrorCategory};
}

namespace micjo {

void MakePhoneCall::execute() {
  // your implementation here
  //
  _errc = PhoneCallError::InvalidNumber;
}

std::error_code MakePhoneCall::popError() {
  std::error_code errc = _errc;
  _errc.clear();
  return errc;
}

std::error_code MakePhoneCall::peekError() { return _errc; }

} // namespace micjo
