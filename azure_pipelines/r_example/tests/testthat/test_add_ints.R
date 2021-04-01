context("simple package - testing foo")

test_that(
    "addition of two integers"
    , {

        expect_equal(
            add_ints(30, 5)
            ,35
        )    

    }
)