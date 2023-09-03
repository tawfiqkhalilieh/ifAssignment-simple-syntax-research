fun main() {
    val a: Int = 5

    // can't build because it's a syntax error
    if (a = 10) {
        println("Hello")
    } else {
        println("No")
    }
}
