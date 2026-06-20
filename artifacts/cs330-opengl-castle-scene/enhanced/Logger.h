/////////////////////////////////////////////////////////////////////////////////
// Logger.h
// ========
// Lightweight structured logger for the CS 330 OpenGL Castle Scene project.
// Provides severity-tagged console output (INFO, WARNING, ERROR) so that
// diagnostic messages can be filtered and traced without a third-party library.
//
// AUTHOR: Francisco Sousa
// Course: CS 499 - Computer Science Capstone, SNHU
// Created: 2026-05-19
// Enhancement: Category One - Software Design and Engineering
/////////////////////////////////////////////////////////////////////////////////

#pragma once
#include <iostream>
#include <string>

class Logger
{
public:
    static void info(const std::string& context, const std::string& message)
    {
        std::cout << "[INFO]  [" << context << "] " << message << std::endl;
    }

    static void warn(const std::string& context, const std::string& message)
    {
        std::cout << "[WARN]  [" << context << "] " << message << std::endl;
    }

    static void error(const std::string& context, const std::string& message)
    {
        std::cerr << "[ERROR] [" << context << "] " << message << std::endl;
    }
};
