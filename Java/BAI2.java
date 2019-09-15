package BAI2;

class SV{
    private String hoTen;
    private int tuoi;
    private float dtb;

    protected void set(String hoTen, int tuoi, float dtb) {
        this.tuoi = tuoi;
        this.hoTen = hoTen;
        this.dtb = dtb;
    }

    protected void show() {
        System.out.println(this.hoTen);
        System.out.println(this.tuoi);
        System.out.println(this.dtb);
    }
}
public class BAI2 {
    public static void main(String[] args) throws Exception {
        SV A = new SV();
        A.set("tieu C", 21, (float)11.11);
        A.show();
    }
}