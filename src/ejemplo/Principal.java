package ejemplo;

public class Principal {
	public static double T,TPLL,TPV,TF;
	public static  void condicionesIniciales() {
		T=0;
		TPLL=IA();
		TPV=Double.MAX_VALUE;
		TF=60000000;
	}
	public static double IA() {
		return 10;// aca va la fpd
	}
	private static void eventoVisitaMedico() {
		T=TPLL;
		TPLL=T+IA();
	}
	public static void eventoLlegadaDePaciente() {
		
	}
	public static void main(String[] args) {
		condicionesIniciales();
		while(T<TF) {
//			System.out.println(TPV);
//			TPV=T;
//			T=10;
//			System.out.println(TPV+";"+T);
			if(TPLL<TPV)eventoLlegadaDePaciente();
			else eventoVisitaMedico();
		}
	}
}
