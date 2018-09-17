l=length(X);
dy1=Der(Y,X,'cd');
dy2=Der(dy1,X(1:l-1),'cd');
plot(X,Y,X(1:l-1),dy1,X(2:l-1),dy2)
legend('orig','1st_der','2nd_der','location','north')