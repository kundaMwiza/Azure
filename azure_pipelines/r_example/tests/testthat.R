library(testthat)
library(simpleRpackage)


if (requireNamespace("xml2")) {
    test_check(
        "simpleRpackage"
        ,reporter = MultiReporter$new(
            reporters = list(
                JunitReporter$new(file = "test-results.xml")
                ,CheckReporter$new()
                )
            )
        )
} else {
    test_check("simpleRpackage")
}