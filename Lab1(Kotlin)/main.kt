import kotlin.math.sqrt

fun main() {
    var a: Double
    var b: Double
    var c: Double

   a = inputCoef("A")
   b = inputCoef("B")
   c = inputCoef("C")
        
   val D = b*b - 4*a*c

   when {
      D > 0 -> {
         val x1 = (-b + sqrt(D)) / (2 * a)
         val x2 = (-b - sqrt(D)) / (2 * a)
         println("x1 = $x1, x2 = $x2")
         }
      D == 0.0 -> {
         val x = -b / (2 * a)
         println("x = $x")
         }
      else -> {
         println("Нет действительных корней")
         }
   }
   
}

fun inputCoef(coef_name: String): Double {
    println("Введите коэффициент $coef_name: ")
    while (true) {
        try {
            return readLine()!!.toDouble()
        } catch (e: NumberFormatException) {
            println("Ошибка. Введите число")
        }
    }
}
