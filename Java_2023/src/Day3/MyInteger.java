package Day3;

public class MyInteger {
    private int integerValue = 0;

    public MyInteger(int m) {
        this.integerValue = m;
    }

    public int getIntegerValue() {
        return integerValue;
    }

    public void setIntegerValue(int integerValue) {
        this.integerValue = integerValue;
    }

    @Override
    public String toString() {
        return integerValue + "";
    }
}
