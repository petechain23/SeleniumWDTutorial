import logging
import loggingpackage.custom_logger as cl

class LoggingDemo2():

    log = cl.customLogger(logging.DEBUG)

    def method1(self):
        self.log.debug("debug message")
        self.log.info("info message")
        self.log.warning("warning message")
        self.log.error("error message")
        self.log.critical("critical message")

    def method2(self):
        log2 = cl.customLogger(logging.INFO)
        log2.debug("debug message")
        log2.info("info message")
        log2.warning("warning message")
        log2.error("error message")
        log2.critical("critical message")

    def method3(self):
        log3 = cl.customLogger(logging.WARNING)
        log3.debug("debug message")
        log3.info("info message")
        log3.warning("warning message")
        log3.error("error message")
        log3.critical("critical message")

demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()