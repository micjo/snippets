#include <thread>
#include <chrono>
#include <condition_variable>
#include <mutex>
#include <iostream>
#include <memory>

#include "thread_example.h"

namespace {
    std::mutex _mutex;
    std::condition_variable _cv;
    bool _killThread{0};

    constexpr const char* threadName = "Thread_1";
}


using namespace std::literals;

ThreadExample::ThreadExample() {}

ThreadExample::~ThreadExample()
{
    {
        std::lock_guard<std::mutex> lock(_mutex);
        _killThread=true;
    }
    std::cout << "Destructor> notifying" << std::endl;
    _cv.notify_all();
}

void ThreadExample::create_and_detach_thread()
{
    std::thread ( []()
    {
        // Make sure thread name is not too long
        pthread_setname_np(pthread_self(), threadName);

        // This obtains the mutex lock
        std::unique_lock<std::mutex> lock(_mutex);

        while (true) {
            // Do things periodically every 5 seconds
            std::cout << threadName << "> doing things" << std::endl;

            // Bail out on destruction. Using predicate to prevent spurious wakeups
            if ( _cv.wait_for(lock, std::chrono::seconds(5), [] {return _killThread;} )) {
                std::cout << threadName << "> got killed" << std::endl;
                break;
            }
        }
    }).detach();
}


int main() {
    {
        auto p = std::make_unique<ThreadExample>();
        p->create_and_detach_thread();
        std::this_thread::sleep_for(500ms);
    }
}
