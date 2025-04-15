#include <streambuf>
#include <istream>

class memorybuffer : public std::streambuf {
public:
    memorybuffer(const char* base, size_t size) {
        char* p = const_cast<char*>(base);
        setg(p, p, p + size);
    }
};

class mstream : public std::istream {
public:
    mstream(const char* data, size_t size)
        : std::istream(&buffer), buffer(data, size) {}

private:
    memorybuffer buffer;
};

